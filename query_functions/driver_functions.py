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
