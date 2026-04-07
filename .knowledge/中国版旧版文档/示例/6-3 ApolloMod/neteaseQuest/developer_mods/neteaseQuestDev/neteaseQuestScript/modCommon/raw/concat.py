# -*- coding: utf-8 -*-

import os
import shutil
import mmap
import sys

PY3 = sys.version_info[0] == 3

DIALOGUE_DATA = {}
QUEST_DATA = {}

for name in [filename[::-1].split('.', 1)[-1][::-1] for filename in os.listdir('.') if filename[-3:] in ('.py', 'pyc') and filename not in ['concat.bat', 'concat.py', 'essentials', '__init__.py']]:
	try:
		DIALOGUE_DATA.update(__import__(name, globals(), locals(), ['DialogueConfig']).DialogueConfig)
	except:
		try:
			QUEST_DATA.update(__import__(name, globals(), locals(), ['QuestConfig']).QuestConfig)
		except:
			if PY3:
				try:
					with open('{}.py'.format(name), 'rb') as f:
						content = f.read().replace(
							b"NPC_ENTITY_ID_DICT.setdefault(v['npcEntityId'], {i: set() for i in xrange(5)})[v['appearCondition']].add(k) for k, v in DialogueConfig.iteritems()",
							b"NPC_ENTITY_ID_DICT.setdefault(v['npcEntityId'], {i: set() for i in range(5)})[v['appearCondition']].add(k) for k, v in DialogueConfig.items()")
					with open('{}.py'.format(name), 'wb') as f:
						f.write(content)
					DIALOGUE_DATA.update(__import__(name, globals(), locals(), ['DialogueConfig']).DialogueConfig)
					continue
				except:
					pass

for filename in ('dialogueConfig.py', 'questConfig.py'):
	shutil.copy('essentials/{}'.format(filename), '..')

f = open("../dialogueConfig.py", "rb+")
data = mmap.mmap(f.fileno(), 0)
while 1:
	line = f.readline()
	if line.startswith(b'# editor config begin'):
		break
p = f.tell()
end = p + 18
start = p + 17
# end = p + 15
# start = p + 14
d = end - start
size = len(data)
data.move(start, end, size - end)
data.flush()
data.close()
f.truncate(size - d)
f.flush()
content = str(DIALOGUE_DATA)[:-1].encode('utf-8')
data = mmap.mmap(f.fileno(), 0)
size = len(data)
data.flush()
data.close()
f.seek(size)
f.write(b"%" * len(content))
f.flush()
data = mmap.mmap(f.fileno(), 0)
data.move(start + len(content), start, size - start)
data.seek(start)
data.write(content)
data.flush()
data.close()
f.flush()
f.close()

f = open("../questConfig.py", "rb+")
data = mmap.mmap(f.fileno(), 0)
while 1:
	line = f.readline()
	if line.startswith(b'# editor config begin'):
		break
p = f.tell()
# end = p + 18
# start = p + 17
end = p + 15
start = p + 14
d = end - start
size = len(data)
data.move(start, end, size - end)
data.flush()
data.close()
f.truncate(size - d)
f.flush()
content = str(QUEST_DATA)[:-1].encode('utf-8')
data = mmap.mmap(f.fileno(), 0)
size = len(data)
data.flush()
data.close()
f.seek(size)
f.write(b"%" * len(content))
f.flush()
data = mmap.mmap(f.fileno(), 0)
data.move(start + len(content), start, size - start)
data.seek(start)
data.write(content)
data.flush()
data.close()
f.flush()
f.close()
