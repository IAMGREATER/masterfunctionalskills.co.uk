#!/usr/bin/env python3
import sys, os
from maths_overhaul_engine import render_maths_topic

import maths_domain1_number
import maths_domain2_finance_ratio
import maths_domain3_measures
import maths_domain4_geometry
import maths_domain5_stats_prob
import maths_extras

all_topics = []
all_topics.extend(maths_domain1_number.TOPICS_DOMAIN1)
all_topics.extend(maths_domain2_finance_ratio.TOPICS_DOMAIN2)
all_topics.extend(maths_domain3_measures.TOPICS_DOMAIN3)
all_topics.extend(maths_domain4_geometry.TOPICS_DOMAIN4)
all_topics.extend(maths_domain5_stats_prob.TOPICS_DOMAIN5)
all_topics.extend(maths_extras.EXTRAS_MATHS)

print(f"Compiling all {len(all_topics)} flagship Maths Revision pages on disk...")

count = 0
for topic in all_topics:
    try:
        render_maths_topic(topic)
        count += 1
    except Exception as e:
        print(f"[ERROR] Failed to compile {topic.get('filename')}: {e}")

print(f"\n==========================================")
print(f"Compilation Complete! Successfully compiled {count} / {len(all_topics)} Maths pages.")
print(f"==========================================")
