import java.util.Vector;

public class Equipo {
	private String nombre;
	private int id;
	private ScrumMaster scrumMaster;
	public Vector<Integrante> integrantes = new Vector<Integrante>();

	public String getNombre() {
		return this.nombre;
	}

	public void setNombre(String aNombre) {
		this.nombre = aNombre;
	}

	public int getId() {
		return this.id;
	}

	public void setId(int aId) {
		this.id = aId;
	}

	public void addIntegrate(Integrante aIntegrante) {
		throw new UnsupportedOperationException();
	}

	public void toString() {
		throw new UnsupportedOperationException();
	}

	public ScrumMaster getScrumMaster() {
		return this.scrumMaster;
	}

	public void setScrumMaster(ScrumMaster aScrumMaster) {
		this.scrumMaster = aScrumMaster;
	}

	public Equipo(int aId, String aNombre, ScrumMaster aSm) {
		throw new UnsupportedOperationException();
	}
}