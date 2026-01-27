import time
from asn1_feedback_correction import right_correction

if __name__ == '__main__':  
    prev_time = 0
    curr_time = time.time()
    right_correction(prev_time, curr_time)