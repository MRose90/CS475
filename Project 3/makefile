proj1:
	g++ -DNUMT=1 proj0.cpp -o proj0 -lm -fopenmp
loop:
	echo "" > 1.csv; \
	echo "" > 2.csv; \
		for numt in 1 2 4; do \
			for padding in 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16; do \
				g++ -DNUMT=$$numt -DNUMPAD=$$padding  fix1.cpp -o fix1 -lm -fopenmp ;\
				./fix1 >>1.csv ; \
				done; \
			g++ -DNUMT=$$numt fix2.cpp -o fix2 -lm -fopenmp ;\
			./fix2 >>2.csv ; \
		done; 
clean:
	rm -f *.o
