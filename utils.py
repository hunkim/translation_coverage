def get_progress_emoji(ratio):
    emoji_list = [':new_moon:', ':waning_crescent_moon:', ':last_quarter_moon:',
                  ':waning_gibbous_moon:', ':full_moon:']

    # Coverage range
    # 0 -- 20 -- 40 -- 60 -- 80 -- 100
    return emoji_list[int(ratio/20.2)]
