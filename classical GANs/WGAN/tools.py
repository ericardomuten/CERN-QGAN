import os
import numpy as np
import matplotlib.pyplot as plt

import h5py
from math import floor
from matplotlib import rc

def create_folder(folder_name):    #create folders in which the trainings progress will be saved
    try:
        # Create target Directory
        os.mkdir(folder_name)
    except FileExistsError:
       pass;
    return

def plot_loss(save_folder, d_loss, g_loss):
    rc('text', usetex=True)
    rc('font', family='serif', size = 25)

    fig = plt.figure(figsize = (10,6))
    time_steps = np.arange(len(g_loss))

    plt.plot(time_steps, d_loss, label = 'Discriminator Loss', linewidth = 2) 
    plt.plot(time_steps, g_loss, label = 'Generator Loss', linewidth = 2)

    plt.legend(loc = 'best', fontsize = 16)
    plt.xlabel("Epoch", fontsize = 20)
    plt.ylabel("Loss", fontsize = 20)

    fig.savefig(os.path.join(save_folder, "loss_plot.png"))

    plt.close()

def plot_error(save_folder, MSE):
    rc('text', usetex=True)
    rc('font', family='serif', size = 25)

    fig = plt.figure(figsize = (10,6))
    time_steps = np.arange(len(MSE))

    plt.plot(time_steps, MSE, linewidth = 2) 

    plt.xlabel("Epoch", fontsize = 20)
    plt.ylabel("MSE", fontsize = 20)

    fig.savefig(os.path.join(save_folder, "MSE_plot.png"))

    plt.close()

def plot_outputs(save_folder, real_data, outputs, epoch, num_to_plot = 100):
    rc('text', usetex=True)
    rc('font', family='serif', size = 20)
    
    fig, ax = plt.subplots(2, 1, figsize = (10,12))
    
    m,n = outputs.shape
    
    x = np.arange(n)
    ax[0].bar(x, np.mean(outputs, axis = 0), label = 'Generated')
    ax[0].plot(x, real_data, 'ro-', linewidth = 2, label = 'Target')
    ax[0].legend() 
    ax[0].set_xlabel("Calorimeter Depth", fontsize = 20)
    ax[0].set_ylabel("Energy (GeV)", fontsize = 20)

    ax[1].plot(x, np.transpose(outputs[:num_to_plot])) 

    ax[1].set_xlabel("Calorimeter Depth", fontsize = 20)
    ax[1].set_ylabel("Energy (GeV)", fontsize = 20)

    title =  "output_plot_epoch" + str(epoch) + ".png"
    fig.savefig(os.path.join(save_folder, title))

    plt.close()



def load_average_data(file_name, nevt, N) : 

    d=h5py.File(file_name,'r')

    xd = d['ECAL'][:]
    print("Original data shape : ", xd.shape)

    nx = xd.shape[2]
    ny = xd.shape[3]

    N2 = ny//N

    X=np.array(xd[:nevt,:,:])


    x_sum = []
    for x in X:
        tmp = np.sum(x[0], axis = 0)
        tmp  = np.array([np.sum(tmp[N2*i:N2*(i+1)])for i in range(floor(len(tmp)/N2))])
    
        x_sum.append(tmp)

    X_train = x_sum
    X_train = np.array(X_train)
    print("Training data shape : ", X_train.shape)
    return X_train