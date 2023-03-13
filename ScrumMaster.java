public class ScrumMaster {
	private String nombre;
	private String rolSecundario;
	public Equipo hasA;

	public String getNombre() {
		return this.nombre;
	}

	public void setNombre(String aNombre) {
		this.nombre = aNombre;
	}

	public String getRolSecundario() {
		return this.rolSecundario;
	}

	public void setRolSecundario(String aRolSecundario) {
		this.rolSecundario = aRolSecundario;
	}

	public ScrumMaster(String aNombre, String aRolSecundario) {
		throw new UnsupportedOperationException();
	}
}