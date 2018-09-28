# NEX Encrypt

NEX encrypt is symmetric-key algorithm for the encryption text using python3 . This algorithm adapted from [DES algorithm](https://en.wikipedia.org/wiki/Data_Encryption_Standard).  

## Usage

 To **encrypt** text create `Nex_encrypt` with *`key`* input :
 
```sh
>>> NE = Nex_encrypt( *key* )
```
you can change your *`key`* with `Nex_encrypt`

```sh
>>> NE.set_key( *key* )
```
then passing the *`text`* to encrypt to `encode` function :

```sh
>>> NE.encrypt( *text* )
```

## Referent

 - J. Orlin Grabbe. *The DES Algorithm Illustrated*. Retrieved  27 September, 2018, Available : [http://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm](http://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm)
 - *Data Encryption Standard*. Retrieved  26 September, 2018, Available : 
[https://en.wikipedia.org/wiki/Data_Encryption_Standard](https://en.wikipedia.org/wiki/Data_Encryption_Standard)
