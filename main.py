import json

with open('script_config.json', 'r') as json_file:
    config = json.load(json_file)

result = config['RESULT']
#system_template = config['SYSTEM_TEMPLET']
#config_template = config['CONFIG_TEMPLET']
#vectoriz = config['SUMMARIZE_VECTORIZER']

def syste_init():
    #output_file_path = "output.txt"

    with open('serve36_remove.json', 'r') as json_file:
        json_data = json.load(json_file)

    with open(f"{result}system.txt", 'w') as txt_file:
        # local_comment commond
        local_comment = dict(json_data["server"][0]['sysSystem']['modules'])
        txt_file.write(f"{local_comment['comment']} \n")

        for item in json_data["server"][0]['sysSystem']['modules']['LOCAL']:
            # print('LOCAL',item.get('id'), item.get('comment'))
            txt_file.write(f"LOCAL {item.get('id')} {item.get('comment')}\n")

        #default comment commond
        txt_file.write("\n")
        default_comment = dict(json_data["server"][0]['sysSystem']['modules']['defaultModule'])
        txt_file.write(f"{default_comment['comment']} \n")

        DEFAULT_MODULE = dict(json_data["server"][0]['sysSystem']['modules']['defaultModule']['DEFAULT_MODULE'])
        txt_file.write(f"DEFAULT_MODULE {DEFAULT_MODULE['id']} \n")


        # NUM_MSGS comment commond
        txt_file.write("\n")
        num_msgs_comment = dict(json_data["server"][0]['sysSystem']['queue']['normalMsgQSize'])
        txt_file.write(f"{num_msgs_comment['comment']} \n")

        NUM_MSGS = dict(json_data["server"][0]['sysSystem']['queue']['normalMsgQSize']['NUM_MSGS'])
        txt_file.write(f"NUM_MSGS {NUM_MSGS['value']}  {NUM_MSGS['comment']} \n")

        # NUM_LMSGS comment commond
        txt_file.write("\n")
        num_lmsgs_comment = dict(json_data["server"][0]['sysSystem']['queue']['longMsgQSize'])
        txt_file.write(f"{num_lmsgs_comment['comment']} \n")

        NUM_LMSGS = dict(json_data["server"][0]['sysSystem']['queue']['longMsgQSize']['NUM_LMSGS'])
        txt_file.write(f"NUM_LMSGS {NUM_LMSGS['value']}  {NUM_LMSGS['comment']} \n")

        # ** CONG_MSG    0xef    10000    60000

        # ** ** ** ** Redirector   Module ID ** ** ** ** ** ** *
        # REDIRECT comment commond
        txt_file.write("\n")
        redirect_comment = dict(json_data["server"][0]['sysSystem']['redirects'])
        txt_file.write(f"{redirect_comment['comment']} \n")

        for item in json_data["server"][0]['sysSystem']['redirects']['REDIRECT']:
            # print('LOCAL',item.get('id'), item.get('comment'))
            txt_file.write(f"REDIRECT {item.get('from')} {item.get('to')} {item.get('comment')}\n")

        # Now start-up all local tasks:
        # FORK_PROCESS comment commond
        txt_file.write("\n")
        fork_process_comment = dict(json_data["server"][0]['sysSystem']['process'])
        txt_file.write(f"{fork_process_comment['comment']} \n")

        for item in json_data["server"][0]['sysSystem']['process']['FORK_PROCESS']:
            # print('LOCAL',item.get('id'), item.get('comment'))
            txt_file.write(f"FORK_PROCESS {item.get('app')} {item.get('args')} {item.get('comment')}\n")

        txt_file.write("\n")
        txt_file.write(f"VERIFY \n")


def Config_latest_sg():

    with open('serve36_remove.json', 'r') as json_file:
        Config_data = json.load(json_file)

    with open(f"{result}config.txt", 'w') as text_file:

        # CNSYS comment commond
        cnsys_comment = dict(Config_data["server"][0]['sysConfig']['global'])
        text_file.write(f"{cnsys_comment['comment']} \n")

        # **** Configure your System IP Addres and Set DAUD=Y
        CNSYS = dict(Config_data["server"][0]['sysConfig']['global']['CNSYS:'])
        text_file.write(f"CNSYS:IPADDR={CNSYS['IPADDR=']},DAUD={CNSYS['DAUD=']},autoact={CNSYS['AUTOACT=']};\n")

        #### *** Configure Your STP IP's and PORT Address and SNEND as S
        # SNSLI comment commond
        text_file.write("\n")
        snsli_comment = dict(Config_data["server"][0]['sysConfig']['sctpAssoc'])
        text_file.write(f"{snsli_comment['comment']} \n")

        for item in Config_data["server"][0]['sysConfig']['sctpAssoc']['SNSLI:']:
            text_file.write(f"SNSLI:SNLINK={item.get('SNLINK=')},IPADDR={item.get('IPADDR=')},HPORT={item.get('HPORT=')},PPORT={item.get('PPORT=')},SNEND={item.get('SNEND=')},SNTYPE={item.get('SNTYPE=')},SG={item.get('SG=')};\n")

        ###### *** Configure System PC and Routing Context
        #SNAPI: AS = 1, OPC = 16127, RC = 0, SS7MD = ITU14, TRMD = LS;
        # SNAPI comment commond
        text_file.write("\n")
        snapi_comment = dict(Config_data["server"][0]['sysConfig']['localAS'])
        text_file.write(f"{snapi_comment['comment']} \n")

        for item in Config_data["server"][0]['sysConfig']['localAS']['SNAPI:']:
            text_file.write(f"SNAPI:AS={item.get('LAS=')},OPC={item.get('OPC=')},RC={item.get('RC=')},SS7MD={item.get('SS7MD=')},TRMD={item.get('TRMD=')};\n")

        # ** Configure your Destination Pointcode and Routing Context at STP end
        #SNRTI:SNRT=1,DPC=16035;
        # SNRIT comment commond
        text_file.write("\n")
        snrit_comment = dict(Config_data["server"][0]['sysConfig']['m3uaRouting'])
        text_file.write(f"{snrit_comment['comment']} \n")

        for item in Config_data["server"][0]['sysConfig']['m3uaRouting']['routes']['SNRTI:']:
            text_file.write(f"SNRTI:SNRT={item.get('SNRT=')},DPC={item.get('DPC=')};\n")

        # * Configure the Signalling Links
        #SNRLI:SNRL=1,SNRT=1,SG=1;
        # SNRLI comment commond
        text_file.write("\n")
        snrli_comment = dict(Config_data["server"][0]['sysConfig']['m3uaRouting']['routesMap'])
        text_file.write(f"{snrli_comment['comment']} \n")

        for item in Config_data["server"][0]['sysConfig']['m3uaRouting']['routesMap']['SNRLI:']:
            text_file.write(f"SNRLI:SNRL={item.get('SNRT=')},SNRT={item.get('SNRT=')},SG={item.get('SG=')};\n")

        # * Map LAS and RAS
        #SNLBI:SNLB=1,LAS=1,SG=1;
        # SNLBI comment commond
        text_file.write("\n")
        snlbi_comment = dict(Config_data["server"][0]['sysConfig']['m3uaRouting']['mapAS'])
        text_file.write(f"{snlbi_comment['comment']} \n")

        for item in Config_data["server"][0]['sysConfig']['m3uaRouting']['mapAS']['SNLBI:']:
            text_file.write(f"SNLBI:SNLB={item.get('SNLB=')},LAS={item.get('LAS=')},SG={item.get('SG=')};\n")

        # MTP_USER_PART
        # MTP_USER_PART comment commond
        text_file.write("\n")
        mtp_user_part_comment = dict(Config_data["server"][0]['sysConfig']['userPart'])
        text_file.write(f"{mtp_user_part_comment['comment']} \n")

        for item in Config_data["server"][0]['sysConfig']['userPart']['MTP_USER_PART']:
            text_file.write(f"MTP_USER_PART {item.get('sio')} {item.get('mid')};\n")

    print("Values from JSON have been inserted into the Text  and saved")











if __name__ == '__main__':
    syste_init()
    Config_latest_sg()
#print("Values from JSON have been inserted into the Text  and saved")
