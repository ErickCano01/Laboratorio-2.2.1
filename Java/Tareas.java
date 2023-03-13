public class Tareas {
	private int id;
	private int prioridad;
	private String contexto;
	public Integrante encargado;

	public void getContexto() {
		throw new UnsupportedOperationException();
	}

	public void setContexto(Object aContexto) {
		throw new UnsupportedOperationException();
	}

	public int getId() {
		return this.id;
	}

	public void setId(int aId) {
		this.id = aId;
	}

	public int getPrioridad() {
		return this.prioridad;
	}

	public void setPrioridad(int aPrioridad) {
		this.prioridad = aPrioridad;
	}

	public void setContexto(String aContexto) {
		this.contexto = aContexto;
	}
}