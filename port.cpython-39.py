a
    �Fb�  �                   @   s�   d dl Z d dlZdZdZdZdZdZdZe�d� e � e j	e j
�Ze�d	� d
d� Zede d e d e �Zeeed e d e ��Zed� edkr�edkr�ee� q�eed� n
eed� dS )�    Nz[31mz[32mz[36mz[35mz[33mz[0m�clear�   c                 C   s,   t �t| f�rtt| d� ntt| d� d S )Nz-> CLOSEz-> OPEN)�sZ
connect_ex�host�print�R�G)�port� r
   �port.py�portScanner   s    r   z[1mz	Ip or URLz >> zPort (1 - 65535)�
i��  �   zPort value is lowzPort value is high)Zsocket�osr   r   �B�P�Y�W�systemZAF_INETZSOCK_STREAMr   Z
settimeoutr   �inputr   �intr	   r   r
   r
   r
   r   �<module>   s&   


