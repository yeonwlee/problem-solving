from typing import Any

#-*- coding: utf-8 -*-
class SimpleDictionary:
    """
    딕셔너리 구현체로, 해시 테이블을 사용하여 키-값 쌍을 저장.
    
    속성:
        _MAX_VALUE_FOR_LOAD_FACTOR (int): 재해싱이 발생하기 전 최대 로드 팩터값. 이 값을 넘어가면 재해싱 진행.
        _MULTIPLY_VALUE_FOR_REHASHING (int): 재해싱 시 버킷 크기를 확장하는 배수.
    
    매개변수:
        default_size (int): 딕셔너리의 초기 버킷 크기. 기본값은 1009로, 소수로 지정함.
    """
    
    _MAX_VALUE_FOR_LOAD_FACTOR: int = 0.7
    _MULTIPLY_VALUE_FOR_REHASHING: int = 2
    
    def __init__(self, default_size: int = 1009):
        self._bucket_size: int = default_size
        self._buckets: list = [[] for index in range(self._bucket_size + 1)]
        self._num_of_keys: int = 0
        
        
    def __len__(self):
        return self._num_of_keys
    
    
    def __setitem__(self, key: Any, value: Any) -> None:
        if self._get_load_factor() > self._MAX_VALUE_FOR_LOAD_FACTOR:
            self._re_hashing()
        self._set_data_in_buckets(self._buckets, key, value)
            
            
    def __getitem__(self, key: Any) -> Any:
        index: int = self._hash(key)
        if self._buckets[index]:
            for bucket_key, bucket_value in self._buckets[index]:
                if bucket_key == key:
                    return bucket_value
        raise KeyError(key)
    
    def __delitem__(self, key: Any) -> None:
        index: int = self._hash(key)
        if self._buckets[index]:
            if len(self._buckets[index]) > 1:
                for bucket_index, bucket_data in enumerate(self._buckets[index]):
                    if bucket_data[0] == key:
                        del self._buckets[index][bucket_index]
                        return
            else:
                self._buckets[index] = []
                self._num_of_keys -= 1
                return
        raise KeyError(key)  
    
    
    def __iter__(self):
        for data in self._buckets:
            for key, value in data:
                yield (key, value)
    
    
    def _set_data_in_buckets(self, buckets: list, key: Any, value: Any) -> None:
        index = self._hash(key)
        if buckets[index]:
            for key_and_value in buckets[index]:
                if key_and_value[0] == key:
                    key_and_value[1] = value
                    return
        buckets[index].append([key, value])
        self._num_of_keys += 1
        
        
    def _get_load_factor(self) -> float:
        return self._num_of_keys / self._bucket_size
    
    
    def _re_hashing(self) -> None:
        self._bucket_size = self._bucket_size * self._MULTIPLY_VALUE_FOR_REHASHING
        self._num_of_keys = 0
        new_buckets = [[] for index in range(self._bucket_size + 1)]
        for key, value in self.__iter__():
           self._set_data_in_buckets(new_buckets, key, value)
        self._buckets = new_buckets
        
        
    def _hash(self, key: Any) -> float:
        return hash(key) % len(self._buckets)
   

