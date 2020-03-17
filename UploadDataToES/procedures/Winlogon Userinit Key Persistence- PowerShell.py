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
                "event_id": "4104"
              }
            },
            {
              "bool": {
                "should": [
                  {
                    "multi_match": {
                      "query": "*Set-ItemProperty*",
                      "fields": [],
                      "type": "phrase"
                    }
                  },
                  {
                    "multi_match": {
                      "query": "*New-Item*",
                      "fields": [],
                      "type": "phrase"
                    }
                  }
                ]
              }
            },
            {
              "multi_match": {
                "query": "*CurrentVersion\\Winlogon*",
                "fields": [],
                "type": "phrase"
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
technique = "Winlogon Helper DLL"
procedure = "Winlogon Userinit Key Persistence- PowerShell"
tech_code = "T1004"

action ={
            "Tatic": tatic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "Count": count,
        }

es.index(index="represent_6",body = action)

