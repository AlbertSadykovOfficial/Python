import redis
import random

conn = redis.Redis()

cats = ['siamse', 'persian', 'maine coon', 'norwegian forest'] # Тема
hats = ['stovepipe', 'bowler', 'tam-o-shanter', 'fedora']

for msg in range(10):
		cat = random.choise(cats)
		hat = random.choise(hats)
		print('Publish: %s wears a %s' % (cat,hat))
		conn.publish(cat, hat)