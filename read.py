def readDataFromFile(filename, delimiter, conversion_func):
	data = []

	with open(filename, 'r') as f:
		data = map(lambda x: conversion_func(x), reduce(lambda x,y: x + y, map(lambda x: x.split(delimiter), f.read().split('\n'))))

	return data
