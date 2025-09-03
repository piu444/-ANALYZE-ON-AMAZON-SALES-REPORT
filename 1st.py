import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import numpy as np , logging , dbConnect

logging.basicConfig(
    filename='Project_bank/logs/logfile.log',
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s'
    filemode="a"
)

