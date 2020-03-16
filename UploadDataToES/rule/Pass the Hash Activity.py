from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc =  {
  "query": {
    "constant_score": {
      "filter": {
        "bool": {
          "must": [
            {
              "bool": {
                "must": [
                  {
                    "match_phrase": {
                      "logon_type": "3"
                    }
                  },
                  {
                    "match_phrase": {
                      "logon_process_name": "ntlmssp"
                    }
                  },
                  {
                    "bool": {
                      "should": [
                        {
                          "match_phrase": {
                            "event_id": "4624"
                          }
                        },
                        {
                          "match_phrase": {
                            "event_id": "4625"
                          }
                        }
                      ]
                    }
                  }
                ]
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
tatic = "Lateral Movement"
technique = "Pass the Hash"
rule_name = "Pass the Hash Activity"
tech_code = "T1175"

action ={
            "Tatic": tatic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Rule": rule_name,
            "Count": count,
        }

es.index(index="represent_5",body = action)

