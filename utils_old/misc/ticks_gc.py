

def ticks_mapper(gen_position_array: list, gc_dataframe):
    """Function that create two arrays for x axe notation: array with tics and array with tick's labels"""

    position = 0
    array_len = len(gen_position_array)
    step = int(array_len / 10)
    ticks_interval = []
    ticks_label = []

    while position < array_len:
        ticks_interval.append(position)
        ticks_label.append(str(int(gc_dataframe.iloc[position]['Genome position'])))
        position += step

    if str(int(gc_dataframe.iloc[array_len - 1]['Genome position'])) not in ticks_label:
        ticks_interval.append(len(gen_position_array))
        ticks_label.append(str(int(gc_dataframe.iloc[array_len - 1]['Genome position'])))

    return ticks_interval, ticks_label
