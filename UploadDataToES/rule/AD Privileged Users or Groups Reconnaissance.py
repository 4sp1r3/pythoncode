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
                "event_id": "4661"
              }
            },
            {
              "bool": {
                "should": [
                  {
                    "match_phrase": {
                      "object_type": "SAM_USER"
                    }
                  },
                  {
                    "match_phrase": {
                      "object_type": "SAM_GROUP"
                    }
                  }
                ]
              }
            },
            {
              "bool": {
                "should": [
                  {
                    "wildcard": {
                      "object_name.keyword": "*-512"
                    }
                  },
                  {
                    "wildcard": {
                      "object_name.keyword": "*-502"
                    }
                  },
                  {
                    "wildcard": {
                      "object_name.keyword": "*-500"
                    }
                  },
                  {
                    "wildcard": {
                      "object_name.keyword": "*-505"
                    }
                  },
                  {
                    "wildcard": {
                      "object_name.keyword": "*-519"
                    }
                  },
                  {
                    "wildcard": {
                      "object_name.keyword": "*-520"
                    }
                  },
                  {
                    "wildcard": {
                      "object_name.keyword": "*-544"
                    }
                  },
                  {
                    "wildcard": {
                      "object_name.keyword": "*-551"
                    }
                  },
                  {
                    "wildcard": {
                      "object_name.keyword": "*-555"
                    }
                  },
                  {
                    "wildcard": {
                      "object_name.keyword": "*admin*"
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
tatic = "Discovery"
technique = "Account Discovery"
rule_name = "AD Privileged Users or Groups Reconnaissance"
tech_code = "T1087"

action ={
            "Tatic": tatic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Rule": rule_name,
            "Count": count,
        }

es.index(index="represent_5",body = action)

