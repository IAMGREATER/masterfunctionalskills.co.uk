#!/usr/bin/env python3
import sys, os
from english_overhaul_engine import render_english_topic

import english_reading_topics
import english_writing_topics
import english_slc_topics
import english_crosscutting_topics

all_topics = []
all_topics.extend(english_reading_topics.READING_TOPICS)
all_topics.extend(english_writing_topics.WRITING_TOPICS)
all_topics.extend(english_slc_topics.SLC_TOPICS)
all_topics.extend(english_crosscutting_topics.CROSSCUTTING_TOPICS)

print(f"Compiling all {len(all_topics)} English Revision pages on disk...")

count = 0
for topic in all_topics:
    try:
        render_english_topic(topic)
        count += 1
    except Exception as e:
        print(f"[ERROR] Failed to compile {topic.get('filename')}: {e}")

print(f"\n==========================================")
print(f"Compilation Complete! Successfully compiled {count} / {len(all_topics)} English pages.")
print(f"==========================================")
