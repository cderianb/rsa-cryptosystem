# rsa-cryptosystem
<h1>How to use</h1>
  <p>create .env file with following keys</p>
  <ol>
  <li>BIT_LENGTH</li>
  <li>PRIVATE_KEY</li>
  <li>PUBLIC_KEY_N</li>
  <li>PUBLIC_KEY_E</li>
  </ol>
  <p>BIT_LENGTH is for generating prime number with expected length</p>
  <p>PRIVATE_KEY, PRIVATE_KEY_N, PRIVATE_KEY_E can be set by choosing the number manually, or by using KeyGenerator.py</p>
<h2>KeyGenerator.py</h2>
  <p>Contain 4 methods that can be used</p>
  <ol>
  <li>is_prime(number:int)->bool : to check whether number is prime or not</li>
  <li>random_prime(bit:int=8)->int : to generate random prime number with length <bit> bit</li>
  <li>generate_key_pair(e:int, P:int=1, Q:int=1) : to generate rsa key pair, with public key E is mandatory</li>
  <li>verify(N, e, d) : to check whether a key pair is a valid rsa key or not</li>    
  </ol>
<h2>Encryption</h2>
  <p>the value of cipher must be 1 < cipher < N </p>
