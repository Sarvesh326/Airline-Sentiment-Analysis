# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 15:40:50 2022

@author: user
"""

from pydantic import BaseModel
# 2. Class which describes input.
class Review(BaseModel):
    text: str 
