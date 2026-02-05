import time
from asn1_feedback_correction import right_correction, inputGains

if __name__ == '__main__':  
    prev_time = 0
    curr_time = time.time()
    inputGains()
    right_correction(prev_time, curr_time)