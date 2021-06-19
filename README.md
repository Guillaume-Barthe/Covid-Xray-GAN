# Covid-Xray-GAN
Generating fake images of covid X-ray to augment the size of the database

This code was written by [BARTHE Guillaume](https://github.com/Guillaume-Barthe/) and is linked to a paper you can read in the pdf document called paper.pdf. This work is based on the CycleGAN model created by [Jun-Yan Zhu](https://github.com/junyanz) and the link to his repository is [here](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix/) 

## Horse2zebra implementation

If you want to take a look at the cycleGan model applied to Horses and Zebras, the parameters I used to produce the results of the paper and the output images are on this [Colab Notebook](https://colab.research.google.com/github/Guillaume-Barthe/Covid-Xray-GAN/blob/main/CycleGAN_horses.ipynb).

## Covid-19 Xrays implementation

The adaptation to the Covid-19 dataset was also implemented on Google Colab and can be found on this [notebook](https://colab.research.google.com/github/Guillaume-Barthe/Covid-Xray-GAN/blob/main/cyclegan_covid.ipynb). Please note that this has been done with Google Colab PRO and a reasonable training lasts more than 12 hrs and therefore cannot be done with Google Colab basic version.

## Preprocessing and plots

The dataset used for the previous implementation is zipped in Covid-Prepross1.zip and is a toy example of the original dataset. Indeed, the original dataset exceeded 25MB and I was unable to put it in this repository. Moreover if you want to check how the preprocessing was done you can look at the jupyer notebook preprocess_image.ipynb. Finally, in my paper a lot of plots were added to check if the loss was decreasing, the snippet of code to plot those losses can be found in metrics.py. It is based on the .txt files that the algorithm outputs.
