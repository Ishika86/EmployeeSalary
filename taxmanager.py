import ast


def taxmanager(entries):
    tax = {}
    for entry in entries:
        for id in entry:
                ann_sal = entry.get(id).get('Annual Salary')

        try:
                file = open("taxfile.txt", "r")

        except FileNotFoundError:
                print("taxfile not found")

        else:
                contents = file.read()
                dict = ast.literal_eval(contents)
                file.close()

                if  ann_sal<700000:
                        tax[id]=int(ann_sal*dict.get("a"))

                elif ann_sal>=700000 and ann_sal<1500000:
                        tax[id]=int(ann_sal*dict.get("b"))

                else:
                        tax[id]=int(ann_sal*0.16)


                file = open("taxlog.txt", "a+")
                logdata = {}
                temp = entry.get(id)
                temp["Tax"] = tax.get(id)

                print(temp["Name"],"of Department",temp["Department"],"with annual salary of", temp["Annual Salary"], "has tax of", temp["Tax"])
                logdata["Name"] = temp["Name"]
                logdata["Department"] = temp["Department"]
                logdata["Annual Salary"] = temp["Annual Salary"]
                logdata["Tax"] = temp["Tax"]

                file.write(str(logdata))
                file.write('\n')
                file.close()
    return tax
