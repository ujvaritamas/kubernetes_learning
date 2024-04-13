#!/bin/bash
for i in {1..20}
do
   result=$(curl http://localhost:8080/counter)
   echo "Result $i: $result"
done