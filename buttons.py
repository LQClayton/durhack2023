import taipy as tp
from taipy import Config, Core, Gui

#Not sure how to generate a button for each word in the file and put on one page

# A first data node configuration to model an input name.
#input_name_data_node_cfg = Config.configure_data_node(id="input_name")
# A second data node configuration to model the message to display.
#message_data_node_cfg = Config.configure_data_node(id="message")
# A task configuration to model the build_message function.
#build_msg_task_cfg = Config.configure_task("build_msg", build_message, input_name_data_node_cfg, message_data_node_cfg)
# The scenario configuration represents the whole execution graph.
#scenario_cfg = Config.configure_scenario("scenario", task_configs=[build_msg_task_cfg])

def file_handle(filename):
    with open(filename, 'r') as f:
        x = f.readlines()
    f.close()
    x = clean_list(x)
    return x

def clean_list(myList):
    for i in range(len(myList)):
        myList[i] = myList[i].replace('\n','')
    return myList

def brain_no_function():
    myFile1 = file_handle('emotions.txt')
    myFile2 = file_handle('phrases.txt')
    print(myFile1, myFile2)

def make_buttons():
    print("hello")
    myFile1 = file_handle('emotions.txt')
    pages = {}
    for element in myFile1:
        print(element)
        #pages[element] = """<|{element}|button|on_action=enlarge|>"""
    print('Hello world')
    print(pages)

make_buttons()

"""
if __name__ == "__main__":
    ################################################################
    #            Instantiate and run Core service                  #
    ################################################################
    Core().run()

    ################################################################
    #            Manage scenarios and data nodes                   #
    ################################################################
    scenario = tp.create_scenario(scenario_cfg)

    ################################################################
    #            Instantiate and run Gui service                   #
    ################################################################

    Gui(pages).run()

"""