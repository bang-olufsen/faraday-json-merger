# faraday-json-merger

Production tool that combines multiple responses to the `Get provisioning data` RACE command into one single JSON file that is ready to be uploaded to the Cloud.

## Getting started

### Dependencies

* Python 3.10+.

---

In order to run the tool, install the dependencies:

```sh
$ python3.10 -m virtualenv venv
$ source venv/bin/activate
$ python -m pip install -r requirements.txt # Note: venv uses python as python3.10
```

### Prerequisites

Before running the tool first you need to have the files containing the response of the RACE command somewhere in your drive. In this example there are three files under the `resources/`.

```txt
.
└── faraday-json-merger/
    ├── json-merger/
    │   └── main.py
    ├── resources/
    │   ├── left
    │   ├── right
    │   └── case
    └── README.md
```

An example of the content of `left` could be:

```txt
7b2264617461223a7b2276223a202231222c2022736e223a20223337313931353430222c202268776964223a20223630413731343045354545384137464430414334394134353934334544454543222c20227061727454797065223a20224c656674222c2022747970654e756d223a202232323434222c20226974656d4e756d223a202231323234343033222c20226877726576223a20223145222c20226465766f7074735f76657273696f6e223a202231222c2022616e63223a207b202272223a2230303030303030303730464530303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030222c20226c223a2230303030303030303730464530303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030227d2c202270726f64756374696f6e223a207b2273697465223a20224368696e61222c20226261746368223a20225056222c202274696d657374616d70223a2022323032342d30342d30315431343a31383a31332e3437355a227d7d2c20227369676e6174757265223a224236444238353636324537354344423638463544363739384132443043434338394336443042353731434541374232304538443343303944303146344242384341344646413132433831343135333245353234313134414533313041324144343733303837343442444532353844434531453643383342453544423233413133227d
```

> 💡 This is just a hex-encoded list of bytes that represent a JSON containing the production data.

### Running the tool

Once you have all the needed files for each part of the set, you can then run the tool in the following way:

```sh
python json-merger/main.py resources/left resources/right resources/case output.json
```

You should see this output in the terminal:

```txt
Decoding 'resources/case'... OK
Decoding 'resources/right'... OK
Decoding 'resources/left'... OK
Merged resources/case, resources/right, resources/left into 'output.json'... OK
```

If so, the process completed successfully. The result will be a JSON file (`output.json` in this case) in plain text that is ready to be uploaded to the Cloud.
