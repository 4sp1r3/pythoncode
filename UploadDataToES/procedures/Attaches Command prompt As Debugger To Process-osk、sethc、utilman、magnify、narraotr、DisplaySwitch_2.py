from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc = {
    "query": {
      "constant_score": {
        "filter": {
          "bool": {
            "must": [
              {
                "match_phrase": {
                  "event_id": "13"
                }
              },
              {
                "bool": {
                  "should": [
                    {
                      "wildcard": {
                        "registry_key_path.keyword": "*\\\\SOFTWARE\\\\Microsoft\\\\Windows NT\\\\CurrentVersion\\\\Image File Execution Options\\\\sethc.exe\\\\Debugger"
                      }
                    },
                    {
                      "wildcard": {
                        "registry_key_path.keyword": "*\\\\SOFTWARE\\\\Microsoft\\\\Windows NT\\\\CurrentVersion\\\\Image File Execution Options\\\\utilman.exe\\\\Debugger"
                      }
                    },
                    {
                      "wildcard": {
                        "registry_key_path.keyword": "*\\\\SOFTWARE\\\\Microsoft\\\\Windows NT\\\\CurrentVersion\\\\Image File Execution Options\\\\osk.exe\\\\Debugger"
                      }
                    },
                    {
                      "wildcard": {
                        "registry_key_path.keyword": "*\\\\SOFTWARE\\\\Microsoft\\\\Windows NT\\\\CurrentVersion\\\\Image File Execution Options\\\\Magnify.exe\\\\Debugger"
                      }
                    },
                    {
                      "wildcard": {
                        "registry_key_path.keyword": "*\\\\SOFTWARE\\\\Microsoft\\\\Windows NT\\\\CurrentVersion\\\\Image File Execution Options\\\\Narrator.exe\\\\Debugger"
                      }
                    },
                    {
                      "wildcard": {
                        "registry_key_path.keyword": "*\\\\SOFTWARE\\\\Microsoft\\\\Windows NT\\\\CurrentVersion\\\\Image File Execution Options\\\\DisplaySwitch.exe\\\\Debugger"
                      }
                    }
                  ]
                }
              },
              {
                "match_phrase": {
                  "event_type": "SetValue"
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
tatic = "Persistence"
technique = "Accessibility Features"
procedure = "Attaches Command prompt As Debugger To Process-osk、sethc、utilman、magnify、narraotr、DisplaySwitch"
tech_code = "T1015"

action ={
            "Tatic": tatic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "Count": count,
        }

es.index(index="represent_6",body = action)

