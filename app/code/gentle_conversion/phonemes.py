import json
import math

from g2p_en import G2p

g2p = G2p()

# file_name = 'G:/Projects/speech aligner/kamal speech aliner/speach_aliner/app/json/json_data_for_frame/kamal.json'
# with open(file_name, 'r') as f:
#   data = json.load(f)


def add_phonemes(data, FRAME_PER_SECOUND=24, EXTRA_TIME=0):
    FRAME_PER_SECOUND = FRAME_PER_SECOUND
    AUDO_END_TIME = data["fragments"][-1]["end"]
    EXTRA_TIME = EXTRA_TIME
    AUDO_END_TIME = math.ceil(float(AUDO_END_TIME) + EXTRA_TIME)

    print("FRAME_PER_SECOUND:", FRAME_PER_SECOUND)
    print("AUDO_END_TIME  : ", AUDO_END_TIME)
    # print(data['fragments'][0])
    for each_data in data.get("fragments"):
        each_data["phonemes"] = g2p(each_data["lines"][0])

        each_data["init_frame"] = math.ceil(
            float(each_data["begin"]) * FRAME_PER_SECOUND
        )
        each_data["final_frame"] = math.ceil(
            float(each_data["end"]) * FRAME_PER_SECOUND
        )

        # each_data['diff'] = math.floor(  (each_data['final_frame'] - each_data['init_frame']) / len(each_data['phonemes']))
        each_data["diff"] = math.ceil(
            (each_data["final_frame"] - each_data["init_frame"])
        )

        number_of_phonemes = len(each_data["phonemes"])
        if number_of_phonemes < each_data["diff"]:
            phonemes_frame = {}
            num, div = each_data["diff"], number_of_phonemes
            count_frame = [num // div + (1 if x < num % div else 0) for x in range(div)]

            for i in range(len(count_frame)):
                phonemes_frame[each_data["phonemes"][i]] = count_frame[i]

        else:
            phonemes_frame = {}
            limited_frame = each_data["diff"]
            for each_phoneme in each_data["phonemes"]:
                if limited_frame > 0:
                    phonemes_frame[each_phoneme] = 1
                    limited_frame -= 1
                else:
                    phonemes_frame[each_phoneme] = 0
        each_data["phonemes_frame"] = phonemes_frame

    data["FRAME_PER_SECOUND"] = FRAME_PER_SECOUND
    data["AUDO_END_TIME"] = AUDO_END_TIME
    data["TOTAL_VIDEO_FRAMES"] = AUDO_END_TIME * FRAME_PER_SECOUND + 1
    data["MODE"] = "normal"

    return data


def returnSum(dict):
    return sum(dict.values())


def equalizer(diff, phonemes_frame):
    """inner sum number vales should be equal to diff"""
    sum = returnSum(phonemes_frame)
    while diff != sum:
        sum = returnSum(phonemes_frame)
        if diff == sum:
            return phonemes_frame
        elif diff <= sum:
            max_value = max(phonemes_frame, key=phonemes_frame.get)
            phonemes_frame[max_value] = phonemes_frame[max_value] - 1
        else:
            max_value = min(phonemes_frame, key=phonemes_frame.get)
            phonemes_frame[max_value] = phonemes_frame[max_value] + 1
    return phonemes_frame


def add_gentle_phonemes(data, gentle_data, FRAME_PER_SECOUND=24, EXTRA_TIME=0):
    gentle_length = len(gentle_data["words"])
    aneaus_length = len(data["fragments"])
    FRAME_PER_SECOUND = FRAME_PER_SECOUND
    AUDO_END_TIME = data["fragments"][-1]["end"]
    EXTRA_TIME = EXTRA_TIME
    AUDO_END_TIME = math.ceil(float(AUDO_END_TIME) + EXTRA_TIME)
    if gentle_length == aneaus_length:
        for counter in range(gentle_length):
            each_data = data["fragments"][counter]
            each_gentle_data = gentle_data["words"][counter]
            each_data["init_frame"] = math.ceil(
                float(each_data["begin"]) * FRAME_PER_SECOUND
            )
            each_data["final_frame"] = math.ceil(
                float(each_data["end"]) * FRAME_PER_SECOUND
            )
            each_data["diff"] = math.ceil(
                (each_data["final_frame"] - each_data["init_frame"])
            )
            # "phonemes_frame": { "K": 2, "EH1": 2, "R": 2 }
            phones = each_gentle_data.get("phones")
            if phones:
                dic_ = {}

                for each_phone in phones:
                    print(each_phone)
                    # { "duration": 0.1, "phone": "ih_B" },
                    dic_[each_phone["phone"]] = math.ceil(
                        float(each_phone["duration"]) * FRAME_PER_SECOUND
                    )
                each_data["phonemes_frame"] = dic_
                each_data["phonemes_frame"] = equalizer(
                    each_data["diff"], each_data["phonemes_frame"]
                )

            # print(counter)
    else:
        print("gentle and aneaus json are not equal")
        return data

    data["FRAME_PER_SECOUND"] = FRAME_PER_SECOUND
    data["AUDO_END_TIME"] = AUDO_END_TIME
    data["TOTAL_VIDEO_FRAMES"] = AUDO_END_TIME * FRAME_PER_SECOUND + 1
    data["MODE"] = "gentle"

    return data


# with open("kamal_phonemes.json", "w") as outfile:
#     json.dump(data, outfile)
