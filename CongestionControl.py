import slidingWindowCC as swCC
import socketTCP as sT
import socketUDP as sU

class CongestionControl:
    def __init__(self, MSS: int):
        self.current_state = "slow start"
        self.MSS = MSS
        self.cwnd = float(self.MSS) 
        self.ssthresh = None

    def get_cwnd(self):
        return int(self.cwnd)

    def get_MSS_in_cwnd(self):
        return int(self.cwnd // self.MSS)

    def event_ack_received(self):
        if self.is_state_slow_start():
            self.cwnd += self.MSS

            if self.ssthresh is not None and self.cwnd >= self.ssthresh:
                self.current_state = "congestion avoidance"

        elif self.is_state_congestion_avoidance():
            mss_in_cwnd = self.get_MSS_in_cwnd()
            if mss_in_cwnd > 0:
                aumento = self.MSS / mss_in_cwnd
                self.cwnd += aumento

    def event_timeout(self):
        self.ssthresh = int(self.cwnd / 2)
        self.cwnd = float(self.MSS)
        self.current_state = "slow start"

    def is_state_slow_start(self):
        return self.current_state == "slow start"
    
    def is_state_congestion_avoidance(self):
        return self.current_state == "congestion avoidance"

    def get_ssthresh(self):
        return self.ssthresh