package clase;

public class masina {
	private String producator;
	private float pret;
	private Combustibil combustibil;
	private int[] distanta;
	
	
	public masina() {
		producator = "";
		pret=5000;
		combustibil = Combustibil.gaz;
		distanta = new int[1];
		distanta[0] = 100;
	}
	
	public masina(String producator, float pret) {
		this.producator=producator;
		this.pret=pret;
		combustibil =Combustibil.gaz;
	}

	public float getPret() {
		return pret;
	}

	public void setPret(float pret) {
		this.pret = pret;
	}

	public Combustibil getCombustibil() {
		return combustibil;
	}

	public void setCombustibil(Combustibil combustibil) {
		this.combustibil = combustibil;
	}

	public String getProducator() {
		return producator;
	}
	
	
}
