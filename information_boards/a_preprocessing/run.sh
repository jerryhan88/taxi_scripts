#!/usr/bin/env bash
for i in 090{1..9} 09{10..11}; do
    python -c "from a2_ap_tripLocation_prevTripEndTime import run; run('$i')" &
done
