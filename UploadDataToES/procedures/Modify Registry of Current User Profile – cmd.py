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
              "wildcard": {
                "registry_key_path.keyword": """*\\CurrentVersion\\Explorer\\Advanced\\HideFileExt*"""
              }
            },
            {
              "match_phrase": {
                "registry_key_value": "DWORD (0x00000001)"
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
tatic = "Defense Evasion"
technique = "Modify Registry"
procedure = "Modify Registry of Current User Profile – cmd"
tech_code = "T1112"

action ={
            "Tatic": tatic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "Count": count,
        }

es.index(index="represent_6",body = action)

