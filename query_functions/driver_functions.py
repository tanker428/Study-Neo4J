from neo4j import GraphDatabase
login = "neo4j"
PASSWORD = 'vrwiki81'
normal = "try"


def flame_difference(label: str, object_name: str, r_type: str, r_type2: str, target_label: str, database: str) -> list:
    query = 'Match (obj:' + label + ")-[r:" + r_type + "]->(bbox1:" + target_label + ")-[r2:" + r_type2 +"]->(bbox2: " + target_label + ") where obj.objectname= \"" + object_name +  '\" return bbox1.flame as bbox1, bbox2.flame as bbox2'
    # print(query)
    DATABASE_URL="bolt://localhost:7687"
    driver = GraphDatabase.driver(DATABASE_URL, auth=("neo4j", PASSWORD))
    session = driver.session(database=database)
    results = session.run(query)
    flame_difference_list = []
    n = 0
    for record in results:
        flame_before = float(record['bbox1'])
        flame_after = float(record['bbox2'])
        flame_difference = flame_after - flame_before
        # print(f"{label}:{object_name}のノードと{r_type}でつながる{target_label}ラベルノードのflame: {flame_before}\n")
        # print(f"またそのノードと{r_type2}でつながる{target_label}ラベルノードのflmae: {flame_after}\n")
        # print(f"flame_difference: {flame_difference}")
        flame_difference_list.append(flame_difference)
        n += 1


    # print(f"base node: {object_name}")
    # print(f"first_relation: {r_type}")
    # print(f"target node label: {target_label}")
    # print(f"second_relation: {r_type2}")
    # print(f"flame_difference_list: {flame_difference_list}")
    print(f"bbox node number: {n}")
    return flame_difference_list

def search_action_and_state_about_object(label: str,object_name: str,  r_type: str, r_type2: str, target_label: str, target_label2: str, database: str):
    query = 'Match (st:' + target_label + ")-[r:" + r_type + "]->(act:" + target_label2 + ")-[r2:" + r_type2 +"]->(obj: " + label + ") where obj.objectname= \"" + object_name +  '\" return st.by as hand, act.event as event'
    DATABASE_URL="bolt://localhost:7687"
    driver = GraphDatabase.driver(DATABASE_URL, auth=("neo4j", PASSWORD))
    session = driver.session(database=database)
    results = session.run(query)
    object_dict = {}
    event_dict = {}
    hand_dict = {}
    hand_dict2 = {}
    hand_dict3 = {}
    hand_dict4 = {}
    
    hand_dict["RHand(Direct)"] = 0
    hand_dict["LHand(DIrect)"] = 0
    hand_dict["times"] = 0

    hand_dict2["RHand(Direct)"] = 0
    hand_dict2["LHand(DIrect)"] = 0
    hand_dict2["times"] = 0

    hand_dict3["RHand(Direct)"] = 0
    hand_dict3["LHand(DIrect)"] = 0
    hand_dict3["times"] = 0

    hand_dict4["RHand(Direct)"] = 0
    hand_dict4["LHand(DIrect)"] = 0
    hand_dict4["times"] = 0

    event_dict["HoverExit"] = hand_dict
    event_dict["HoverEnter"] = hand_dict2
    event_dict["SelectEnter"] = hand_dict3
    event_dict["SelectExit"] = hand_dict4

    for record in results:
        event = record['event']
        hand = record['hand']
        # print(f"event: {event}")
        # print(f"hand; {hand}")
        if event == "HoverEnter":
            hand_dict["times"] += 1
            hand_dict[hand] += 1
            # print("a")
        elif event == "HoverExit":
            hand_dict2["times"] += 1
            hand_dict2[hand] += 1
            # print("b")
        elif event == "SelectEnter":
            hand_dict3["times"] += 1
            hand_dict3[hand] += 1
            # print("c")
        elif event == "SelectExit":
            hand_dict4["times"] += 1
            hand_dict4[hand] += 1
            # print("d")
        # print(event_dict)

    object_dict[object_name] = event_dict
    print(object_dict)
    return object_dict

#########################################################################################################

def search_all_action_and_state_about_object(label: str, object_list: str, r_type: str, r_type2: str, target_label: str, target_label2: str, database: str):
    object_information_list = []
    object_list_size = len(object_list)
    for i in range(object_list_size):
        object_dict = search_action_and_state_about_object(label, object_list[i], r_type, r_type2, target_label, target_label2, database)
        object_information_list.append(object_dict)
    print(f"object_list: {object_information_list}")
    return object_information_list

def all_flame_difference_mean(label: str, object_list: list, r_type: str, r_type2: str, target_label: str, database: str) -> dict:
    list_size = len(object_list)
    flame_difference_all_dict = {}
    flame_difference_dict = {}
    # flame_mean_list = []
    # flame_label_list = []
    for i in range(list_size):
        object_name = object_list[i]
        flame_dif_list = flame_difference(label, object_name, r_type, r_type2, target_label, database)
        flame_dif_list_size = len(flame_dif_list)
        flame_dif_list_sum = sum(flame_dif_list)
        if flame_dif_list_sum == 0:
            flame_dif_list_mean = 0
        else:
            flame_dif_list_mean = flame_dif_list_sum / flame_dif_list_size
        flame_difference_all_dict[object_name] = {"size":flame_dif_list_size, "sum":flame_dif_list_sum, "mean":flame_dif_list_mean}
        flame_difference_dict[object_name] = flame_dif_list_mean
        

    print(f"flame_difference_dict: {flame_difference_dict}")
    return flame_difference_all_dict, flame_difference_dict
