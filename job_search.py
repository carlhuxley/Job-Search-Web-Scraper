# -*- coding: utf-8 -*-
"""
Created on Fri May 17 10:24:32 2019

@author: Carl Huxley

This code web scrapes job details from cwjobs.co.uk. and exports a csv file.
"""
from job_func import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)