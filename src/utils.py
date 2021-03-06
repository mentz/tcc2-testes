import time


def purgeContainers(dockerClient):
  # Remover contêineres
  for ct in dockerClient.containers.list(all=True):
    ct.remove(force=True)


def purgeUserNetworks(dockerClient):
  # Remover redes de usuário
  dockerClient.networks.prune()


def timePrint(string):
  now = time.localtime()
  print('[%4d-%02d-%02d %2d:%02d:%02d] %s' %
        (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min,
         now.tm_sec, string))


def waitThenCleanup(ct1, ct2):
  ct1.reload()
  while ct1.status != 'exited':
    time.sleep(1)
    ct1.reload()
  # Encerrar e eliminar contêineres
  time.sleep(1)
  ct2.remove(force=True)
  ct1.remove()
  time.sleep(1)


def waitThenCleanup3(ct1, ct2, ct3):
  ct1.reload()
  while ct1.status != 'exited':
    time.sleep(1)
    ct1.reload()
  # Encerrar e eliminar contêineres
  time.sleep(1)
  ct3.remove(force=True)
  ct2.remove(force=True)
  ct1.remove()
  time.sleep(1)


def waitThenCleanup4(ct1, ct2, ct3, ct4):
  ct1.reload()
  while ct1.status != 'exited':
    time.sleep(1)
    ct1.reload()
  # Encerrar e eliminar contêineres
  time.sleep(1)
  ct4.remove(force=True)
  ct3.remove(force=True)
  ct2.remove(force=True)
  ct1.remove()
  time.sleep(1)
