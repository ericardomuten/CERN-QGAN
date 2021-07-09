<div align="center">
  
# CERN openlab Summer Student Project:<br>Quantum Generative Adversarial Networks
  
  <a href="https://openlab.cern/quantum" target="_blank"><img src="https://img.shields.io/badge/CERN-2021-0033A0?style=flat&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAMAAABHPGVmAAAALVBMVEVHcEz7vQD7vQD8vQD7vQD8vQD7vQD8vQD8vQD7vQD7vQD8vQD7vQD7vQD7vQAgxtLpAAAADnRSTlMAZvVQ6QrVPhl6oSmHvzL6LQUAAASGSURBVHjatdnZdusgDAVQELMY%2Fv9zb2%2Bwc%2BIKDzQLvTXB3gYBFqmaDVeKU4sCBlFyy43WqLjlBpR1BpR1BpR1xjoFxmIFBpSVBpSVBpSVBpSVBpQ1xvdK1oPgblhfOWltjNaJq7ddYT2IfImYJqMDrENUChGDZn%2FWQ%2FMHxBcD4BMyBc5XCHkNQTq60vfIgXAx5xByju6T8V8itsT3%2FUPi6r39Ce8rp%2FCWYrHfIDXs95FZJs%2FvTob6Z4T2buQE4eikvHeG%2FoZY7TpRfDsNWzrjtP0L4s12NYhh%2BO1ZjJ9HfOjdYGo3QZx7YvwEAgOPdx3eQJlArMFA3wXSZ%2BwMQvplJGoPY6sqNU0gxcGYUVx5jtSIx3oS6HysTxEbMMDPAmkM9iFSXnPXt8nwuQ%2FYI8TH%2F425TQe7%2FnBPEH2bECI6T4t%2Bgvh4N1istR50FJdeIX1Ek%2FqJdGGQOWmAa4u7rn18vuuIzUq52gbxvpiSuzIau%2BuO9FUUfTvvCjcoQ4MMltRnEOqF0pdD%2FwiBZWxoqGCn8r2VGKIUCHOoTyHK2g7y1bsJRRqNe3%2FlXv5GbNhWEWXxbsf1UITRF4kYcM4KiI%2FbeFIevNNq7P2EIg0bVL%2BfqCcyYV2rbDdExWSPjUPPGBRh9JTowTscW0Dqf%2BwLXGmPthgKKMJo1f1OSQ29hf1Mbdlmg5NFV1H7KoICA3mruIQ4vl4TTFhvuAlxxrdb1J55KMJoBatEPCv6mr3sJzK%2F9RQKDAx49Ji5ctSLwsxAxgyuiduOAeVtIG14zppPKtAka9lcMZz71IHyNoAcCpvIx6UfxGLleCim3ggUpe0dQhe7I86mWvQERZmCIocryAqPsdYOSQlVIjCgyMRbLSaXxi3GD4LEw4AipzCyyvS5a5ThMpJTGAYUuQljhiWL53R11FN5BxhQsK0UWbE747E7evGV2FaEAUWmDave0H4LQxg6nErl1IEBBRdmOzjkBPpdqFB%2BpUtUGb0tDKloZP44hQLthQoDwXYiXlowpMJIymExdARL8SViYzymhGEMFR%2FR3cOyNoRCpQcZFu1s6AsNhlQuSiJP%2B1Kk90dNRHW9BYyhwlszhNgdb05CjmGcKDb3DotAoYIYV9wWxjDSZcHNmN%2Fj0KpPm3R7dMjq7HlrSokvjIqjww3SEhb4XJDpg3CLvM9%2BPG%2FMHOcaOwzYRFScNe8QHJb9nOEDhvkGwV48eZC3BgfzWwSHZaXthKEVMvkMaQnKhKESzSCkJ37uQqlJ7RmCIcbr%2By5qUEjiIwQK3q4yZKHqYDxEUIo4U6%2BNahxKr0kEZwv8HC%2BDqo69UaI2ieBAujN2RNhOoPybQjBr9oNSKNXSoQ%2B2luCUQuk1iSCIg9oiZl24Vv8TtXLROaotAtO3%2F9ooWSFcjDnH6BQio2SZQSRz%2FpsPfsifQ2RY1tmNBM3oxQRCbRjkOZn%2FEACT2J%2B1vkZiGESyG1SZS%2FqJ1wTogE1hEFHNh9yNCbvvREwqCwwoawwoKw0oKw0oKw0oKw0oKw0oKw0oMFYqMFYqMFYqMBYq88Y%2FxB7wiOJRvWkAAAAASUVORK5CYII%3D" /></a>

  <a href="https://qml-hep.github.io/qml_web/data/" target="_blank"><img alt="ttH Feynman Diagram" height="400px" src="https://raw.githubusercontent.com/eraraya-ricardo/CERN-QGAN/main/assets/ttH_feyndiag.png" /></a>
  
</div>

## Supervisor
[Dr. Sofia Vallecorsa](https://inspirehep.net/authors/1028732)

## Datasets[[1](#references)]
- [Downloads](https://qml-hep.github.io/qml_web/downloads/)
- [Visualization](https://qml-hep.github.io/qml_web/norm/)
- [Data Variable Details & Definitions](https://qml-hep.github.io/qml_web/data/)

## Weekly Progress
- Week 1: Preprocessed the [optimal *ttH* dataset](https://drive.google.com/file/d/1qI-H4q8KGDggUg8YGMtrOGePfeCVGirx/view) (finding the two b-jets in the dataset with highest *pt*). Using this dataset, trained [Su Yeon's classical GANs](https://github.com/QML-HEP/qGAN/blob/main/1_classical_benchmark/ClassicalGAN.ipynb) and (modified) DijetGAN[[2](#references)].
- Week 2: (on progress).

A specific weekly To-Do list is made every week as an [issue](https://github.com/eraraya-ricardo/CERN-QGAN/issues), covering all the comments and suggestions received during Friday meeting. When all the tasks in the To-Do list are done, the issue is marked as closed.

## References
[1] [Vasileios Belis, Samuel González-Castillo, Christina Reissel, Sofia Vallecorsa, Elías F. Combarro, Günther Dissertori, & Florentin Reiter. (2021). Higgs analysis with quantum classifiers.](https://arxiv.org/abs/2104.07692)

[2] [Di Sipio, R., Giannelli, M. F., Haghighat, S. K., &amp; Palazzo, S. (2019). DijetGAN: a Generative-Adversarial Network approach for the simulation of QCD dijet events at the LHC. Journal of High Energy Physics, 2019(8).](https://link.springer.com/article/10.1007/JHEP08(2019)110)
