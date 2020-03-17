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
                "process_command_line": "vssadmin.exe Delete Shadows"
              }
            },
            {
              "match_phrase": {
                "process_command_line": "vssadmin.exe create shadow /for=C:"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "copy \\\\\\\\?\\\\GLOBALROOT\\\\Device\\\\*\\\\windows\\\\ntds\\\\ntds.dit"
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "copy \\\\\\\\?\\\\GLOBALROOT\\\\Device\\\\*\\\\config\\\\SAM"
              }
            },
            {
              "match_phrase": {
                "process_command_line": "vssadmin delete shadows /for=C:"
              }
            },
            {
              "match_phrase": {
                "process_command_line": "reg SAVE HKLM\\SYSTEM "
              }
            },
            {
              "wildcard": {
                "process_command_line.keyword": "esentutl.exe /y /vss *\\\\ntds.dit*"
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
tatic = "Credential Access"
technique = "Credential Dumping"
procedure = "Registry dump of SAM, creds, and secrets"
tech_code = "T1003"

action ={
            "Tatic": tatic,
            "Technique": technique,
            "Tech_code": tech_code,
            "Procedure": procedure,
            "Count": count,
        }

es.index(index="represent_6",body = action)

