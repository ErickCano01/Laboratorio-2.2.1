import java.util.Vector;

public class Integrante {
	private String nombre;
	private String rol;
	public Equipo has;
	public Vector<Tareas> tareas = new Vector<Tareas>();

	public String getNombre() {
		return this.nombre;
	}

	public void setNombre(String aNombre) {
		this.nombre = aNombre;
	}

	public String getRol() {
		return this.rol;
	}

	public void setRol(String aRol) {
		this.rol = aRol;
	}

	public void toString() {
		throw new UnsupportedOperationException();
	}

	public Integrante(String aNombre, String aRol) {
		throw new UnsupportedOperationException();
	}
}