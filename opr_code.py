import requests, sys, json
num = sys.argv[1]
r = requests.get('https://joloapi.com/jolo_tracker_localgrab.php?mobileRange='+num)
j = json.loads(r.text)
opr_code = int(j['operator_code'])
def get_opr_name(opr_code):
    switcher = {
        28: "Airtel",
        1: "Aircel",
        3: "BSNL Special",
        24: "BSNL",
        8: "Idea",
        22: "Vodafone",
        17: "Docomo GSM",
        25: "Docomo GSM Special",
        18: "Docomo CDMA (Indicom)",
        13: "Reliance GSM",
        12: "Reliance CDMA",
        10: "MTS",
        19: "Uninor",
        26: "Uninor Special",
        9: "Loop Mobile",
        5: "Videocon",
        27: "Videocon Special",
        6: "MTNL Mumbai",
        7: "MTNL Mumbai Special",
        20: "MTNL Delhi",
        21: "MTNL Delhi Special",
        30: "Virgin GSM",
        31: "Virgin GSM Special",
        32: "Virgin CDMA",
        33: "T24",
        34: "T24 Special"
        
    }
    return switcher.get(opr_code, "Unknown Operator")
print get_opr_name(opr_code)




'''
This can also be use if the same code is use in json 

<input name="searchTxt" type="text" maxlength="512" id="searchTxt" class="searchField"/>

<script>
    var input = document.getElementById("searchTxt");

    function searchURL() {
         window.location = "http://www.myurl.com/search/" + input.value;
    }
</script>
'''




