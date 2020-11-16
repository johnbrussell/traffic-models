from collections import namedtuple


IntersectionInfo = namedtuple(
    "IntersectionInfo",
    [
        "approach_1_l", "approach_1_s", "approach_1_r",
        "approach_2_l", "approach_2_s", "approach_2_r",
        "approach_3_l", "approach_3_s", "approach_3_r",
        "approach_4_l", "approach_4_s", "approach_4_r",
        "cross_a_b", "cross_a_d", "cross_b_c", "cross_c_d"
    ]
)
IntersectionSize = namedtuple(
    "IntersectionSize",
    [
        "approach_1_l", "approach_1_s", "approach_1_r",
        "approach_2_l", "approach_2_s", "approach_2_r",
        "approach_3_l", "approach_3_s", "approach_3_r",
        "approach_4_l", "approach_4_s", "approach_4_r",
        "depart_1", "depart_2", "depart_3", "depart_4"
    ]
)
IntersectionVolume = namedtuple(
    "IntersectionVolume",
    [
        "approach_1_l", "approach_1_s", "approach_1_r",
        "approach_2_l", "approach_2_s", "approach_2_r",
        "approach_3_l", "approach_3_s", "approach_3_r",
        "approach_4_l", "approach_4_s", "approach_4_r",
        "cross_a_b", "cross_a_d", "cross_b_c", "cross_c_d", "cross_a_c", "cross_b_d"
    ]
)
