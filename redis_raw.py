import redis

redis_conn = redis.Redis(host='localhost', port=6379, db=0)

# para insert e update
redis_conn.set('chave_2', 'troquei')

print(redis_conn.get('chave_2').decode('utf-8'))


### Comandos para hash
meu_hash = {'campo_1': 'valor_1', 'campo_2': 'valor_2'}

redis_conn.hset(name='meu_hash', mapping=meu_hash)

print(redis_conn.hget('meu_hash', 'campo_1').decode('utf-8'))

print(redis_conn.hgetall('meu_hash'))

### Busca por existência
print(redis_conn.hexists('meu_hash', 'campo_1'))


###
# dados -> TTL (time to live)
redis_conn.set('chave_3', 'valor_3', ex=10)
