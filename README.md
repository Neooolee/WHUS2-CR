# WHUS2-CR
This is a Sentinel-2A cloud removal dataset in which the paired cloud and cloud-free images are from different regions of the world. The types of land cover are rich and the acquisition dates of the experimental data cover a long time period (from 2015 to 2019) and all seasons.
The details of the dataset are introduced in datadoc.docx
The dataset can be downloaded on: http://doi.org/10.5281/zenodo.5607356.  
https://pan.baidu.com/s/1pqiQIX8ikRwJpke9z1BltQ.  Extraction code: s2cr.  
***We would suggest to use the new Sentinel-2A cloud removal dataset WHUS2-CRv: https://github.com/Neooolee/WHUS2-CRv.

The environmental dependencies are listed in CRMSS.yml. Researchers can re-produce the training dataset by running cutimg.py.

Distributions of training and testing data. Training areas are marked in white, testing areas are marked in black. The landcover background is derived from 300 m annual global land cover time series from 1992 to 2015 (Defourny et al., 2017)  
![WHUS2-CR.png](https://i.loli.net/2020/12/23/XSh6YCA23fnMQiZ.png)  

If you use this dataset for your research, please cite us accordingly:  
#Reference:
[1]J. Li, Z. W, Z. Hu, J. Z, M. Li, L. Mo and M. Molinier, “Thin cloud removal in optical remote sensing images based on generative adversarial networks and physical model of cloud distortion,” ISPRS J. Photogramm. Remote Sens., vol. 166, pp. 373-389, Aug. 2020,http://doi.org/10.1016/j.isprsjprs.2020.06.021.
[2]J. Li, Z. Wu, Z. Hu, Z. Li, Y. Wang, and M. Molinier, “Deep learning based thin cloud removal fusing vegetation red edge and short wave infrared spectral information for Sentinel-2A imagery,” Remote Sens., vol. 13, no. 1, p. 157, Jan. 2021, http://doi.org/10.3390/rs13010157.
[3]J. Li, Y. Zhang, Q. Sheng, Z. Wu, B. Wang, Z. Hu, G. Shen, M. Schmitt, M. Molinier, “Thin Cloud Removal Fusing Full Spectral and Spatial Features for Sentinel-2 Imagery,” in IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing, vol. 15, pp. 8759-8775, 2022,http://doi.org/10.1109/JSTARS.2022.3211857.

