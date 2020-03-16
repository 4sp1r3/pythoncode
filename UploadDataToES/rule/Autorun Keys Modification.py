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
                      "registry_key_path.keyword": "*\\\\SOFTWARE\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Run*"
                    }
                  },
                  {
                    "wildcard": {
                      "registry_key_path.keyword": "*\\\\software\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\RunOnce*"
                    }
                  },
                  {
                    "wildcard": {
                      "registry_key_path.keyword": "*\\\\software\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\RunOnceEx*"
                    }
                  },
                  {
                    "wildcard": {
                      "registry_key_path.keyword": "*\\\\software\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\RunServices*"
                    }
                  },
                  {
                    "wildcard": {
                      "registry_key_path.keyword": "*\\\\software\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\RunServicesOnce*"
                    }
                  },
                  {
                    "wildcard": {
                      "registry_key_path.keyword": "*\\\\software\\\\Microsoft\\\\Windows NT\\\\CurrentVersion\\\\Winlogon\\\\Userinit*"
                    }
                  },
                  {
                    "wildcard": {
                      "registry_key_path.keyword": "*\\\\software\\\\Microsoft\\\\Windows NT\\\\CurrentVersion\\\\Winlogon\\\\Shell*"
                    }
                  },
                  {
                    "wildcard": {
                      "registry_key_path.keyword": "*\\\\software\\\\Microsoft\\\\Windows NT\\\\CurrentVersion\\\\Windows*"
                    }
                  },
                  {
                    "wildcard": {
                      "registry_key_path.keyword": "*\\\\software\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Explorer\\\\User Shell Folders*"
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
tatic = "Persistence"
technique = "Registry Run Keys / Startup Folder"
rule_name = "Autorun Keys Modification"
tech_code = "T1060"

action ={
            "Tatic": tatic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Rule": rule_name,
            "Count": count,
        }

es.index(index="represent_5",body = action)

