def is_haiku(input_string):
    line = input_string.split('/')

    line_num = len(line)
    if line_num == 3:
        #line_1 = line[0]
        #line_2 = line[1]
        #line_3 = line[2]
        line_1_syllables = line[0].split(',')
        l1_syllables_num = len(line_1_syllables)
        if l1_syllables_num == 5:
            line_2_syllables = line[1].split(',')
            if len(line_2_syllables) == 7:
                line_3_syllables = line[2].split(',')
                if len(line_3_syllables) == 5:
                    sample_string=True
                else:
                    sample_string='WARNING: The third line is not 5 syllables long.\nFalse'
            else:
                sample_string='WARNING: The second line is not 7 syllables long.\nFalse'
        else:
            sample_string='WARNING: The first line is not 5 syllables long.\nFalse'
    else:
        sample_string='WARNING: Sample_input_string dose not 3 lines.\nFalse'

    return sample_string
def haiku_string_parser(haiku_string):
    haiku=is_haiku(haiku_string)
    final_format=""

    if haiku==True:
        haiku_string=haiku_string.split('/')
        #print(haiku_string)
        line1 = haiku_string[0]
        line2 = haiku_string[1]
        line3 = haiku_string[2]

        line1.split(' ')
        line1 = ''.join(line1)
        line1 = line1.split(",")
        new_line1 = "".join(line1)

        line2.split(' ')
        line2 = ''.join(line2)
        line2 = line2.split(",")
        new_line2 = "".join(line2)

        line3.split(' ')
        line3 = ''.join(line3)
        line3 = line3.split(",")
        new_line3 = "".join(line3)

        #final_format
        final_format+=new_line1+'\n'+new_line2+'\n'+new_line3

    else:
        final_format+=""
    return final_format

def main():
    sample_input_string = input('sample_string: ')
    haiku_string = is_haiku(sample_input_string)
    print(haiku_string)
    formatted_haiku = haiku_string_parser(sample_input_string)
    print(formatted_haiku)
main()
# "clouds ,mur,mur ,dark,ly /it ,is , a , blin,ding ,ha,bit /ga,zing ,at ,the ,moon "
# "clouds murmur darkly
# it is  a  blinding habit
# gazing at the moon "