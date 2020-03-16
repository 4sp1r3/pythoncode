from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc = {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "should": [
            {
              "match_phrase": {
                "param3": "* -NoP -sta -NonI -W Hidden -Enc *"
              }
            },
            {
              "match_phrase": {
                "param3": "* -noP -sta -w 1 -enc *"
              }
            },
            {
              "match_phrase": {
                "param3": "* -NoP -NonI -W Hidden -enc *"
              }
            }
          ]
        }
      }
    }
  }
}

res = es.search(index="logs-endpoint-winevent-*",body=doc)

count = res['hits']['total']['value']
tatic = "Execution"
technique = "PowerShell"
rule_name = "Detects suspicious powershell command line parameters used in Empire"
tech_code = "T1086"

action ={
            "Tatic": tatic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Rule": rule_name,
            "Count": count,
        }

es.index(index="represent_5",body = action)

