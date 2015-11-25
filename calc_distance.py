#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

class CalcDistance:

    def __init__(self, api_key):
        self.api_key = api_key

    def main(self):
        persons = [{"adress":"lädersättravägen 13"},{"adress":"ballonggatan 7"},{"adress":"åsögatan 194"},{"adress":"norrtullsgatan 31"},{"adress":"lostigen 52"},{"adress":"ringstensgatan 25"},{"adress":"sturegatan 44"}]

        persons = self.calculate_all_distances(persons)

        self.print_total_distance(persons, "bicycling")
        self.print_total_distance(persons, "driving")
        self.print_total_distance(persons, "walking")
        self.print_total_distance(persons, "transit")

    def calculate_all_from_adress(self, adress):
        persons = [{"adress": adress}]
        persons = self.calculate_all_distances(persons)
        return persons

    def calculate_all_distances(self, persons):
        persons = self.calculate_distance(persons, "bicycling")
        persons = self.calculate_distance(persons, "driving")
        persons = self.calculate_distance(persons, "walking")
        persons = self.calculate_distance(persons, "transit")

        return persons


    def calculate_distance(self, persons, mode):

        origins = ""
        for person in persons:
            origins += person["adress"].replace(" ", "+") + "|"

        r = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + origins + "&destinations=Hantverkargatan+5+Stockholm&mode=" + mode + "&language=en-EN&key=" + self.api_key)

        if r.status_code != requests.codes.ok:
            print("failed request")
            exit()

        data = json.loads(r.text)

        for i in range(0,len(data["rows"])):
            persons[i][mode] = {}
            persons[i][mode]["distance"] = data["rows"][i]["elements"][0]["distance"]["value"]
            persons[i][mode]["duration"] = data["rows"][i]["elements"][0]["duration"]["text"]

        return persons


    def print_total_distance(self, persons, type):
        sum = 0

        for person in persons:
            sum += int(person[type]["distance"])
        print("distance for " + type + " is " + str(sum))
