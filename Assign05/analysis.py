# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 11:49:11 2020

@author: clems
"""

import math
import numpy as np
from PIL import Image
import cv2
class Analysis:
    def __init__(self,overt_file, covert_file):
        overt_file = Image.open(overt_file)
        overt_file.load()
        self.overt = np.asarray_chkfinite(overt_file, dtype="int32")
        covert_file = Image.open(covert_file)
        covert_file.load()
        self.covert = np.asarray_chkfinite(covert_file, dtype="int32")
        
    def ssim(self):
        img1 = self.overt
        img2 = self.covert
        
        C1 = (0.01 * 255)**2
        C2 = (0.03 * 255)**2
    
        img1 = img1.astype(np.float64)
        img2 = img2.astype(np.float64)
        kernel = cv2.getGaussianKernel(11, 1.5)
        window = np.outer(kernel, kernel.transpose())
    
        mu1 = cv2.filter2D(img1, -1, window)[5:-5, 5:-5]  # valid
        mu2 = cv2.filter2D(img2, -1, window)[5:-5, 5:-5]
        mu1_sq = mu1**2
        mu2_sq = mu2**2
        mu1_mu2 = mu1 * mu2
        sigma1_sq = cv2.filter2D(img1**2, -1, window)[5:-5, 5:-5] - mu1_sq
        sigma2_sq = cv2.filter2D(img2**2, -1, window)[5:-5, 5:-5] - mu2_sq
        sigma12 = cv2.filter2D(img1 * img2, -1, window)[5:-5, 5:-5] - mu1_mu2
    
        ssim_map = ((2 * mu1_mu2 + C1) * (2 * sigma12 + C2)) / ((mu1_sq + mu2_sq + C1) *
                                                                (sigma1_sq + sigma2_sq + C2))
        return ssim_map.mean()
    
    
    def calculate_ssim(self):
        img1 = self.overt
        img2 = self.covert
        '''calculate SSIM
        the same outputs as MATLAB's
        img1, img2: [0, 255]
        '''
        if not img1.shape == img2.shape:
            raise ValueError('Input images must have the same dimensions.')
        if img1.ndim == 2:
            return self.ssim()
        elif img1.ndim == 3:
            if img1.shape[2] == 3:
                ssims = []
                for i in range(3):
                    ssims.append(self.ssim())
                return np.array(ssims).mean()
            elif img1.shape[2] == 1:
                self.overt = np.squeeze(img1)
                self.covert = np.squeeze(img2)
                return self.ssim()
        else:
            raise ValueError('Wrong input image dimensions.')
            
    def calculate_psnr(self):
        img1 = self.overt
        img2 = self.covert
        # img1 and img2 have range [0, 255]
        img1 = img1.astype(np.float64)
        img2 = img2.astype(np.float64)
        mse = np.mean((img1 - img2)**2)
        if mse == 0:
            return float('inf')
        return 20 * math.log10(255.0 / math.sqrt(mse))