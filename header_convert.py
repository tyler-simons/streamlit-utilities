import streamlit as st
import re

header_text = """GET /finder/api/v1/explorer-service/dining-availability/%7BC3E99747-0916-4D30-A94F-0505F5655C14%7D/dlr/19268344;entityType=restaurant/table-service/3/2022-10-10/?mealPeriod=80000712 HTTP/2
    Host: disneyland.disney.go.com
    User-Agent: Mozilla/2.0 (Macintosh; Intel Mac OS X 10.10; rv:154.0) Gecko/22200101 Firefox/106.0
    Accept: application/json, text/plain, */*
    Accept-Language: en_US
    Accept-Encoding: gzip, deflate, br
    undefined: e3d56e20-45a1-11ed-b4bb-afc2341a
    DNT: 1
    Connection: keep-alive
    Referer: https://disneyland.disney.go.com/dining/disneyland/ogas-cantina/availability-modal
    Cookie: [object Object]
    Sec-Fetch-Dest: empty
    Sec-Fetch-Mode: cors
    Sec-Fetch-Site: same-origin
    TE: trailers"""


def create_headers(header_string):
    """Convert a string of headers from firefox to a python dict"""
    values = "(?<=: )[^\n]+"
    keys = "(?<=\\n)[^:]+"
    key_list = [i.strip() for i in re.findall(keys, header_string)]
    value_list = [i.strip() for i in re.findall(values, header_string)]

    headers = {k: v for k, v in zip(key_list, value_list)}
    return headers


st.title("Header2Dict :rocket:")
st.subheader("Paste your headers below for quick and easy conversion to use in python")

header_input = st.text_area("Paste your headers here", header_text)
headers = create_headers(header_input)
st.write(headers)
