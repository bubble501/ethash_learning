import ethash

def int_to_bytes(i):
    b = []
    for _ in range(32):
        b.append(chr(i & 0xff))
        i >>= 8
    b.reverse()
    return "".join(b)

def main():
    block_number = 300001
    easy_difficulty = int_to_bytes(2**256 - 1)
    seed = ethash.get_seedhash_by_block_number(block_number)
    header = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

    cache_size = ethash.get_cache_size(block_number)
    full_size = ethash.get_full_size(block_number)
    print "calculate cache ...."
    cache = ethash.mkcache(cache_size, seed)
    print "calculate dataset..."
    dataset = ethash.calc_dataset(full_size, cache)
    print "mining..."
    result = ethash.mine(full_size, dataset, header, difficulty)
    print "finished..."
    print result
    #cache = ethash.mkcache(1024, "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

main()
