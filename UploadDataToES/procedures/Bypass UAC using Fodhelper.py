from elasticsearch import Elasticsearch

es = Elasticsearch('helk-elasticsearch:9200')

doc = {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "event_id": "13"
          }
        },
        {
          "wildcard": {
            "registry_key_path.keyword":"*\\\\ms-settings\\\\shell\\\\open\\\\command\\\\*"
          }
        }
      ]
    }
  }
}

res = es.search(index="logs-endpoint-winevent-*",body=doc)

count = res['hits']['total']['value']
tatic = "Privilege Escalation"
technique = "Bypass User Account Control"
procedure = "Bypass UAC using Fodhelper"
tech_code = "T1088"

action ={
            "Tatic": tatic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "Count": count,
        }

es.index(index="represent_6",body = action)

