PEDESTRIAN_WALK_SPEED_MPH = 3
PEDESTRIANS_PER_HOUR_RANGE = range(1, 10800)  # 6 usages
PEDESTRIANS_PER_HOUR_INCREMENT = 1.097322
CARS_PER_HOUR_PER_LANE_RANGE = range(1, 3600)  # 12 usages
CARS_PER_LANE_HOUR_INCREMENT = 1.085333
CAR_LANE_WIDTH_FT = 11
CROSSWALK_WIDTH_FT = 6
CAR_TURN_SPEED_MPH = 12.5
CAR_LENGTH = 15
PEDESTRIAN_LENGTH = 1
MINIMUM_LIGHT_CYCLE_SEC = 3
MONTE_CARLO_SIMULATION_SEC = 24 * 60 * 60
NUM_LANES_RANGE = range(0, 2)  # 16 usages
LPI_RANGE = range(0, 5)  # 4 usages
FEET_PER_MILE = 5280
SECONDS_PER_HOUR = 3600
YELLOW_LIGHT_SEC = 3
GREEN_LIGHT_DELAY_SEC = 1
EXISTENCE_RANGE = [True, False]  # 41 usages
LIGHT_CYCLE_RANGE = range(0, 120)  # 16 usages
MIN_DELAY_AFTER_DETECT_RANGE = range(0, 15)  # 16 usages

# 10000^6 = 1x10^24
# 3600^12 = 4.738x10^42 = 4.738x10^66
# 3^16 = 4.305x10^7 = 2.04x10^74
# 6^4 = 1.296x10^3 = 2.643x10^77
# 2^41 = 2.199x10^12 = 5.813x10^89
# 121^16 = 2.111x10^33 = 1.227x10^123
# 16^16 = 1.845x10^19 = 2.264x10^142 => there are this many possible configurations of intersection and traffic volume

# Potential concepts to consider:
# Dedicated pedestrian signal (part of cycle once)
# Dedicated pedestrian signal (part of cycle, multiple times per cycle (eg. after every traffic phase))
# Dedicated pedestrian signal (beg; immediate)
# Dedicated pedestrian signal (beg; cars go first)
# Dedicated pedestrian signal (beg; cars both lanes go first)
# Dedicated pedestrian signal (beg; peds always go after same traffic)
# Simultaneous pedestrian signal (no beg)
# Simultaneous pedestrian signal (one begs, other doesn't)
# Simultaneous pedestrian signal (both beg)
# One lane dedicated simultaneous, other begs for all crossings (immediate)
# One lane dedicated simultaneous, other begs for all crossings (wait one cycle)
# One lane dedicated simultaneous, other begs for all crossings (wait two cycles)
# One lane dedicated simultaneous, other begs for all crossings (peds always go after same traffic)
# One lane begs for simultaneous, other begs for all crossings (immediate)
# One lane begs for simultaneous, other begs for all crossings (wait one cycle)
# One lane begs for simultaneous, other begs for all crossings (wait two cycles)
# One lane begs for simultaneous, other begs for all crossings (peds always go after same traffic)
# Everything is by request
# Dedicated pedestrian cycle is default
# Ped volume
# Car volume
# LPI range
# Light cycle range
# Ped time range
# Is ped cycle long enough for diagonal crossing?
# Can ped cycle be activated upon beg if sufficient time remains in light cycle?
# Is light cycle shorter without simultaneous ped cycle?
# Turn lanes
# Has signalized slip lane for turn
# Ped can come on any corner, have a destination of any corner
# Each approach one way to, one way away, or two way
# Number of lanes per direction per approach
# Yellow light can activate ped signal
# Ped crossing exists
# Dedicated turning phases exist (and how long are they)
# Opposite car phases overlap
# Is light cycle dedicated or by request
# Delay after traffic detect before light cycle turns off


def analyze_naive():
    # Incurs an IndentationError for too many levels of indentation, but should provide inputs for all possible
    #  three and four way intersections
    for lanes_away_1 in NUM_LANES_RANGE:
        for lanes_away_2 in NUM_LANES_RANGE:
            for lanes_away_3 in NUM_LANES_RANGE:
                for lanes_away_4 in NUM_LANES_RANGE:
                    for lanes_to_l_1 in NUM_LANES_RANGE:
                        for lanes_to_s_1 in NUM_LANES_RANGE:
                            for lanes_to_r_1 in NUM_LANES_RANGE:
                                for lanes_to_l_2 in NUM_LANES_RANGE:
                                    for lanes_to_s_2 in NUM_LANES_RANGE:
                                        for lanes_to_r_2 in NUM_LANES_RANGE:
                                            for lanes_to_l_3 in NUM_LANES_RANGE:
                                                for lanes_to_s_3 in NUM_LANES_RANGE:
                                                    for lanes_to_r_3 in NUM_LANES_RANGE:
                                                        for lanes_to_l_4 in NUM_LANES_RANGE:
                                                            for lanes_to_s_4 in NUM_LANES_RANGE:
                                                                for lanes_to_r_4 in NUM_LANES_RANGE:
                                                                    for peds_per_hour_a_b in PEDESTRIANS_PER_HOUR_RANGE:
                                                                        for peds_per_hour_a_c in PEDESTRIANS_PER_HOUR_RANGE:
                                                                            for peds_per_hour_a_d in PEDESTRIANS_PER_HOUR_RANGE:
                                                                                for peds_per_hour_b_c in PEDESTRIANS_PER_HOUR_RANGE:
                                                                                    for peds_per_hour_b_d in PEDESTRIANS_PER_HOUR_RANGE:
                                                                                        for peds_per_hour_c_d in PEDESTRIANS_PER_HOUR_RANGE:
                                                                                            for cars_per_lane_hour_1_l in CARS_PER_HOUR_PER_LANE_RANGE:
                                                                                                for cars_per_lane_hour_1_s in CARS_PER_HOUR_PER_LANE_RANGE:
                                                                                                    for cars_per_lane_hour_1_r in CARS_PER_HOUR_PER_LANE_RANGE:
                                                                                                        for cars_per_lane_hour_2_l in CARS_PER_HOUR_PER_LANE_RANGE:
                                                                                                            for cars_per_lane_hour_2_s in CARS_PER_HOUR_PER_LANE_RANGE:
                                                                                                                for cars_per_lane_hour_2_r in CARS_PER_HOUR_PER_LANE_RANGE:
                                                                                                                    for cars_per_lane_hour_3_l in CARS_PER_HOUR_PER_LANE_RANGE:
                                                                                                                        for cars_per_lane_hour_3_s in CARS_PER_HOUR_PER_LANE_RANGE:
                                                                                                                            for cars_per_lane_hour_3_r in CARS_PER_HOUR_PER_LANE_RANGE:
                                                                                                                                for cars_per_lane_hour_4_l in CARS_PER_HOUR_PER_LANE_RANGE:
                                                                                                                                    for cars_per_lane_hour_4_s in CARS_PER_HOUR_PER_LANE_RANGE:
                                                                                                                                        for cars_per_lane_hour_4_r in CARS_PER_HOUR_PER_LANE_RANGE:
                                                                                                                                            for light_cycle_1_l_time_sec in LIGHT_CYCLE_RANGE:
                                                                                                                                                for light_cycle_1_s_time_sec in LIGHT_CYCLE_RANGE:
                                                                                                                                                    for light_cycle_1_r_time_sec in LIGHT_CYCLE_RANGE:
                                                                                                                                                        for light_cycle_2_l_time_sec in LIGHT_CYCLE_RANGE:
                                                                                                                                                            for light_cycle_2_s_time_sec in LIGHT_CYCLE_RANGE:
                                                                                                                                                                for light_cycle_2_r_time_sec in LIGHT_CYCLE_RANGE:
                                                                                                                                                                    for light_cycle_3_l_time_sec in LIGHT_CYCLE_RANGE:
                                                                                                                                                                        for light_cycle_3_s_time_sec in LIGHT_CYCLE_RANGE:
                                                                                                                                                                            for light_cycle_3_r_time_sec in LIGHT_CYCLE_RANGE:
                                                                                                                                                                                for light_cycle_4_l_time_sec in LIGHT_CYCLE_RANGE:
                                                                                                                                                                                    for light_cycle_4_s_time_sec in LIGHT_CYCLE_RANGE:
                                                                                                                                                                                        for light_cycle_4_r_time_sec in LIGHT_CYCLE_RANGE:
                                                                                                                                                                                            for ped_cycle_a_b_sec in LIGHT_CYCLE_RANGE:
                                                                                                                                                                                                for ped_cycle_a_d_sec in LIGHT_CYCLE_RANGE:
                                                                                                                                                                                                    for ped_cycle_b_c_sec in LIGHT_CYCLE_RANGE:
                                                                                                                                                                                                        for ped_cycle_c_d_sec in LIGHT_CYCLE_RANGE:
                                                                                                                                                                                                            for lpi_a_b in LPI_RANGE:
                                                                                                                                                                                                                for lpi_a_d in LPI_RANGE:
                                                                                                                                                                                                                    for lpi_b_c in LPI_RANGE:
                                                                                                                                                                                                                        for lpi_c_d in LPI_RANGE:
                                                                                                                                                                                                                            for crossing_a_b_activates_with_sufficient_time in EXISTENCE_RANGE:
                                                                                                                                                                                                                                for crossing_a_d_activates_with_sufficient_time in EXISTENCE_RANGE:
                                                                                                                                                                                                                                    for crossing_b_c_activates_with_sufficient_time in EXISTENCE_RANGE:
                                                                                                                                                                                                                                        for crossing_c_d_activates_with_sufficient_time in EXISTENCE_RANGE:
                                                                                                                                                                                                                                            for light_1_l_longer_with_peds in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                for light_1_s_longer_with_peds in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                    for light_1_r_longer_with_peds in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                        for light_2_l_longer_with_peds in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                            for light_2_s_longer_with_peds in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                                for light_2_r_longer_with_peds in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                                    for light_3_l_longer_with_peds in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                                        for light_3_s_longer_with_peds in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                                            for light_3_r_longer_with_peds in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                                                for light_4_l_longer_with_peds in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                                                    for light_4_s_longer_with_peds in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                                                        for light_4_r_longer_with_peds in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                                                            for slip_lane_a in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                                                                for slip_lane_b in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                                                                    for slip_lane_c in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                                                                        for slip_lane_d in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                                                                            for can_detect_on_yellow in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                                                                                for cross_a_b_exists in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                                                                                    for cross_a_d_exists in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                                                                                        for cross_b_c_exists in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                                                                                            for cross_c_d_exists in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                                                                                                for light_1_l_requests in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                                                                                                    for light_1_s_requests in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                                                                                                        for light_1_r_requests in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                                                                                                            for light_2_l_requests in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                                                                                                                for light_2_s_requests in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                                                                                                                    for light_2_r_requests in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                                                                                                                        for light_3_l_requests in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                                                                                                                            for light_3_s_requests in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                                                                                                                                for light_3_r_requests in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                                                                                                                                    for light_4_l_requests in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                                                                                                                                        for light_4_s_requests in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                                                                                                                                            for light_4_r_requests in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                                                                                                                                                for cross_a_b_begs in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                                                                                                                                                    for cross_a_d_begs in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                                                                                                                                                        for cross_b_c_begs in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                                                                                                                                                            for cross_c_d_begs in EXISTENCE_RANGE:
                                                                                                                                                                                                                                                                                                                                                                                                for light_1_l_delay_after_alternate_detect in MIN_DELAY_AFTER_DETECT_RANGE:
                                                                                                                                                                                                                                                                                                                                                                                                    for light_1_s_delay_after_alternate_detect in MIN_DELAY_AFTER_DETECT_RANGE:
                                                                                                                                                                                                                                                                                                                                                                                                        for light_1_r_delay_after_alternate_detect in MIN_DELAY_AFTER_DETECT_RANGE:
                                                                                                                                                                                                                                                                                                                                                                                                            for light_2_l_delay_after_alternate_detect in MIN_DELAY_AFTER_DETECT_RANGE:
                                                                                                                                                                                                                                                                                                                                                                                                                for light_2_s_delay_after_alternate_detect in MIN_DELAY_AFTER_DETECT_RANGE:
                                                                                                                                                                                                                                                                                                                                                                                                                    for light_2_r_delay_after_alternate_detect in MIN_DELAY_AFTER_DETECT_RANGE:
                                                                                                                                                                                                                                                                                                                                                                                                                        for light_3_l_delay_after_alternate_detect in MIN_DELAY_AFTER_DETECT_RANGE:
                                                                                                                                                                                                                                                                                                                                                                                                                            for light_3_s_delay_after_alternate_detect in MIN_DELAY_AFTER_DETECT_RANGE:
                                                                                                                                                                                                                                                                                                                                                                                                                                for light_3_r_delay_after_alternate_detect in MIN_DELAY_AFTER_DETECT_RANGE:
                                                                                                                                                                                                                                                                                                                                                                                                                                    for light_4_l_delay_after_alternate_detect in MIN_DELAY_AFTER_DETECT_RANGE:
                                                                                                                                                                                                                                                                                                                                                                                                                                        for light_4_s_delay_after_alternate_detect in MIN_DELAY_AFTER_DETECT_RANGE:
                                                                                                                                                                                                                                                                                                                                                                                                                                            for light_4_r_delay_after_alternate_detect in MIN_DELAY_AFTER_DETECT_RANGE:
                                                                                                                                                                                                                                                                                                                                                                                                                                                for ped_a_b_delay_after_alternate_detect in MIN_DELAY_AFTER_DETECT_RANGE:
                                                                                                                                                                                                                                                                                                                                                                                                                                                    for ped_a_d_delay_after_alternate_detect in MIN_DELAY_AFTER_DETECT_RANGE:
                                                                                                                                                                                                                                                                                                                                                                                                                                                        for ped_b_c_delay_after_alternate_detect in MIN_DELAY_AFTER_DETECT_RANGE:
                                                                                                                                                                                                                                                                                                                                                                                                                                                            for ped_c_d_delay_after_alternate_detect in MIN_DELAY_AFTER_DETECT_RANGE:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                pass


analyze_naive()
